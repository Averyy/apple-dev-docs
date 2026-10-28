# documentationGeneration()

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

The plugin generates documentation.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
static func documentationGeneration() -> PluginCommandIntent
```

## Return Value

A `PluginCommandIntent` instance.

## Discussion

The intent of the command is to generate documentation, either by parsing the package contents directly or by using the build system support for generating symbol graphs. Invoked by a `generate-documentation` verb to `swift package`.

## See Also

### Creating a Command Intent
- [static func sourceCodeFormatting() -> PluginCommandIntent](./sourcecodeformatting%28%29.md)
  The plug-in formats source code.
- [case custom(verb: String, description: String)](./custom%28verb,description%29.md)
  A custom command plug-in intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/plugincommandintent/documentationgeneration())*