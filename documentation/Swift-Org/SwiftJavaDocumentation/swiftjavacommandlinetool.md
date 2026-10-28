---
url: "https://docs.swift.org/latest/documentation/swiftjavadocumentation/swiftjavacommandlinetool"
framework: "Swift-Org/SwiftJavaDocumentation"
---

# swift-java

**Framework**: Swift-Org/SwiftJavaDocumentation  
**Role**: Article

The `swift-java` command line tool offers multiple ways to interact with your Java interoperability enabled projects.

## Overview

The `swift-java` command line tool offers multiple modes which you can use to prepare your Swift and Java code to interact with each other.

When in doubt, you can always use the command line `--help` to get additional guidance about the tool and available options:

```txt
> swift-java --help

OVERVIEW: Generate sources and configuration for Swift and Java
interoperability.

USAGE: swift-java <subcommand>

OPTIONS:
  -h, --help              Show help information.

SUBCOMMANDS:
  configure               Configure and emit a swift-java.config file based on
                          an input dependency or jar file
  resolve                 Resolve dependencies and write the resulting
                          swift-java.classpath file
  wrap-java               Wrap Java classes with corresponding Swift bindings.
  jextract                Wrap Swift functions and types with Java bindings,
                          making them available to be called from Java

  See 'swift-java help <subcommand>' for detailed help.
```

### Expose Java classes to Swift: swift-java wrap-java

`swift-java` uses Java’s runtime reflection facilities to translate the requested Java classes into their Swift projections. The output is a number of Swift source files, one per Java class. You can see its help with:

```bash
swift-java help wrap-java
```

to produce help output like the following:

```txt
> swift-java wrap-java --help

OVERVIEW: Wrap Java classes with corresponding Swift bindings.

USAGE: swift-java wrap-java [<options>] --swift-module <swift-module>

OPTIONS:
  -o, --output-directory <output-directory>
                          The directory in which to output generated SwiftJava
                          configuration files.
  --input-swift <input-swift>
                          Directory containing Swift files which should be
                          extracted into Java bindings. Also known as
                          'jextract' mode. Must be paired with --output-java
                          and --output-swift.
  -l, --log-level <log-level>
                          Configure the level of logs that should be printed
                          (values: trace, debug, info, notice, warning, error,
                          critical; default: log level)
  --config <config>       A path to a custom swift-java.config to use
  --cp, --classpath <cp>  Class search path of directories and zip/jar files
                          from which Java classes can be loaded.
  --swift-module <swift-module>
                          The name of the Swift module into which the resulting
                          Swift types will be generated.
  --depends-on <depends-on>
                          A swift-java configuration file for a given Swift
                          module name on which this module depends,
                          e.g.,
                          JavaUtil=Sources/JavaStdlib/JavaUtil/swift-java.config.
                          There should be one of these
                          options for each Swift module that this module
                          depends on (transitively) that contains
                          wrapped Java sources.
  --swift-native-implementation <swift-native-implementation>
                          The names of Java classes whose declared native
                          methods will be implemented in Swift.
  --cache-directory <cache-directory>
                          Cache directory for intermediate results and other
                          outputs between runs
  --swift-match-package-directory-structure <swift-match-package-directory-structure>
                          Match java package directory structure with generated
                          Swift files (default: false)
  --single-swift-file-output <single-swift-file-output>
                          If specified, a single Swift file will be generated
                          containing all the generated code
  --filter-include <filter-include>
                          While scanning a classpath, inspect ONLY types
                          included in these packages
  --filter-exclude <filter-exclude>
                          While scanning a classpath, skip types which match
                          the filter prefix. You can exclude specific methods
                          by using the `com.example.MyClass#method` format.
  --android-api-version-file <android-api-version-file>
                          Path to Android api-versions.xml for generating
                          @available attributes based on API level data
  -h, --help              Show help information.
```

For example, the `JavaUtilJar` module in this repository is generated with this command line:

```bash
swift-java wrap-java \
  --swift-module JavaStdlib/JavaUtilJar \
  -o Sources/JavaStdlib/JavaUtilJar/generated \
  --config Sources/JavaStdlib/JavaUtilJar/swift-java.config \
  --depends-on SwiftJava=Sources/SwiftJava/swift-java.config \
  --depends-on JavaUtil=Sources/JavaStdlib/JavaUtil/swift-java.config
```

See `scripts/wrap-java-generate.sh` for the full set of invocations used to regenerate the bundled Java standard library bindings.

The `--swift-module` parameter is the name of the Swift module the code is generated into.

Each `--depends-on` option takes `<swift module name>=<swift-java.config path>` and tells swift-java which other Java classes have already been translated to Swift. For example, if your Java class uses `java.net.URL`, include `JavaNet`’s configuration file as a dependency here.

The `-o` option specifies the output directory. Typically this is `Sources/<module name>/generated` or similar, to keep the generated Swift files separate from hand-written ones. To see the output on the terminal rather than writing files to disk, pass `-` for this option.

The `--config` option points at the `swift-java.config` file listing the classes to translate and their corresponding Swift type names. The tool outputs a single `.swift` file for each class, along with warnings for any public API that cannot be translated into Swift. The most common warnings are due to missing Swift projections for Java classes. For example, here we have not translated (or provided the translation manifests for) the Java classes `java.util.zip.ZipOutputStream` and `java.io.OutputStream`:

```
warning: Unable to translate 'java.util.jar.JarOutputStream' superclass: Java class 'java.util.zip.ZipOutputStream' has not been translated into Swift
warning: Unable to translate 'java.util.jar.JarOutputStream' constructor: Java class 'java.io.OutputStream' has not been translated into Swift
warning: Unable to translate 'java.util.jar.JarInputStream' method 'transferTo': Java class 'java.io.OutputStream' has not been translated into Swift
```

Such warnings mean that some information won’t be statically available in Swift: the superclass won’t be known (so it is assumed to be `JavaObject`), or the affected constructors and methods won’t be translated. If you don’t need those APIs, the warnings can be safely ignored. The APIs can still be called dynamically via JNI.

### Scan a Jar file: swift-java configure –jar

`swift-java configure --jar` scans the given input Jar file for all public classes and writes a `swift-java.config` file mapping every Java class in the Jar to a Swift type. Use it to import an entire Java jar’s API surface, and then invoke `swift-java wrap-java` with the generated configuration file to produce the Swift wrappers.

## See Also

### Source Generation
- [swift-java jextract](./swiftjavajextract.md)
  Automatic Java wrappers for existing Swift code, generated by `swift-java jextract`.
- [swift-java wrap-java](./swiftjavawrapjava.md)
  Automatic Swift wrappers for existing Java code, generated by `swift-java wrap-java`.
- [swift-java resolve](./swiftjavaresolve.md)
  Download Java dependencies for use in Swift builds.
- [SwiftPM Plugin](./swiftpmplugin.md)
  The swift-java SwiftPM plugins automate `swift-java` command line tool invocations during the build.
- [swift-java.config](./swiftjavaconfigfile.md)
  SwiftJava tools can be configured using the `swift-java.config` file.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/swiftjavadocumentation/swiftjavacommandlinetool)*