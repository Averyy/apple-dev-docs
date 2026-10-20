# PluginCommandIntent.custom(verb:description:)

**Framework**: PackageDescription  
**Kind**: case  
**Role**: Case

A custom command plug-in intent.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
case custom(verb: String, description: String)
```

#### Discussion

Use this case when none of the predefined cases fulfill the role of the plug-in.

## Parameters

- `verb`: The invocation verb of the plug-in.
- `description`: A human readable description of the plug-in’s role.

## See Also

### Creating a Command Intent
- [static func documentationGeneration() -> PluginCommandIntent](./documentationgeneration%28%29.md)
  The plugin generates documentation.
- [static func sourceCodeFormatting() -> PluginCommandIntent](./sourcecodeformatting%28%29.md)
  The plug-in formats source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/plugincommandintent/custom(verb:description:))*