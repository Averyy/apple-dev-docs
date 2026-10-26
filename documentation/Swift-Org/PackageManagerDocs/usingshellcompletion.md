---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/usingshellcompletion"
framework: "Swift-Org/PackageManagerDocs"
---

# Using shell completion scripts

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Customize your shell to automatically complete swift package commands.

#### Overview

Package manager ships with completion scripts for Bash, Zsh, and Fish. Generate completion lists for your shell in order to use it.

##### Bash

Use the following commands to install the Bash completions to `~/.swift-package-complete.bash` and automatically load them using your `~/.bash_profile` file.

```bash
swift package completion-tool generate-bash-script > ~/.swift-package-complete.bash
echo -e "source ~/.swift-package-complete.bash\n" >> ~/.bash_profile
source ~/.swift-package-complete.bash
```

Alternatively, add the following commands to your `~/.bash_profile` file to directly load completions:

```bash
# Source Swift completion
if [ -n "`which swift`" ]; then
    eval "`swift package completion-tool generate-bash-script`"
fi
```

##### Zsh

Use the following commands to install the Zsh completions to `~/.zsh/_swift`. You can chose a different folder, but the filename should be `_swift`. This will also add `~/.zsh` to your `$fpath` using your `~/.zshrc` file.

```bash
mkdir ~/.zsh
swift package completion-tool generate-zsh-script > ~/.zsh/_swift
echo -e "fpath=(~/.zsh \$fpath)\n" >> ~/.zshrc
compinit
```

## See Also

### Building Packages
- [Creating a Swift package](./creatingswiftpackage.md)
  Bundle executable or shareable code into a standalone Swift package.
- [Setting the Swift tools version](./settingswifttoolsversion.md)
  Define the minimum version of the swift compiler required for your package.
- [Using build configurations](./usingbuildconfigurations.md)
  Control the build configuration for your app or package.
- [Packaging based on the version of Swift](./swiftversionspecificpackaging.md)
  Provide a package manifest for a specific version of Swift.
- [Bundling resources with a Swift package](./bundlingresources.md)
  Add resource files to your Swift package and access them in your code.
- [Releasing and publishing a Swift package](./releasingpublishingapackage.md)
  Share a specific version of your package.
- [Generating Software Bill of Materials (SBOM)](./generatingsboms.md)
  Create an inventory of components and dependencies using SBOM documents.
- [Continuous Integration Workflows](./continuousintegration.md)
  Build Swift packages with an existing continuous integration setup and prepare apps that consume package dependencies within an existing CI pipeline.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/usingshellcompletion)*