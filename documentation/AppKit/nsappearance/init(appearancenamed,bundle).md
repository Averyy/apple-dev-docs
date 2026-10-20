# init(appearanceNamed:bundle:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates an appearance object from the named appearance file located in the specified bundle.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init?(appearanceNamed name: NSAppearance.Name, bundle: Bundle?)
```

```objc
- (instancetype) initWithAppearanceNamed:(NSAppearanceName) name bundle:(NSBundle *) bundle;
```

#### Return Value

An initialized appearance object, or `nil` if an error occurs.

## Parameters

- `name`: The name of the appearance file to retrieve. Do not include any path information in the name.
- `bundle`: The bundle in which to search for the named appearance file. Specify `nil` to search for the appearance file in the main bundle.

## See Also

### Creating an Appearance
- [init?(named: NSAppearance.Name)](./init%28named%29.md)
  Creates an appearance object based on the name of one of the standard system appearances.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/init(appearancenamed:bundle:))*