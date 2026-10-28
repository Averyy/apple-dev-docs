# sourceCodeFormatting()

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

The plug-in formats source code.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
static func sourceCodeFormatting() -> PluginCommandIntent
```

## Return Value

A `PluginCommandIntent` instance.

## Discussion

The intent of the command is to modify the source code in the package based on a set of rules. Invoked by a `format-source-code` verb to `swift package`.

## See Also

### Creating a Command Intent
- [static func documentationGeneration() -> PluginCommandIntent](./documentationgeneration%28%29.md)
  The plugin generates documentation.
- [case custom(verb: String, description: String)](./custom%28verb,description%29.md)
  A custom command plug-in intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/plugincommandintent/sourcecodeformatting())*