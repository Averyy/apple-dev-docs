# init(appearanceNamed:bundle:)

**Framework**: AppKit  
**Kind**: init

Creates an appearance object from the named appearance file located in the specified bundle.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init?(appearanceNamed name: NSAppearance.Name, bundle: Bundle?)
```

#### Return Value

An initialized appearance object, or `nil` if an error occurs.

## Parameters

- `name`: The name of the appearance file to retrieve. Do not include any path information in the name.
- `bundle`: The bundle in which to search for the named appearance file. Specify   to search for the appearance file in the main bundle.

## See Also

- [init?(named: NSAppearance.Name)](nsappearance/init(named:).md)
  Creates an appearance object based on the name of one of the standard system appearances.
- [init?(coder: NSCoder)](nsappearance/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/init(appearancenamed:bundle:))*