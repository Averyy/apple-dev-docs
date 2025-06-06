# init(named:)

**Framework**: AppKit  
**Kind**: init

Creates an appearance object based on the name of one of the standard system appearances.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init?(named name: NSAppearance.Name)
```

#### Return Value

A standard [`NSAppearance`](nsappearance.md) object.

#### Discussion

When you specify a standard appearance name—such as [`aqua`](nsappearance/name-swift.struct/aqua.md)—this method returns a built-in appearance.

## Parameters

- `name`: The name of a standard appearance. See   for the list of standard appearance names.

## See Also

- [init?(appearanceNamed: NSAppearance.Name, bundle: Bundle?)](nsappearance/init(appearancenamed:bundle:).md)
  Creates an appearance object from the named appearance file located in the specified bundle.
- [init?(coder: NSCoder)](nsappearance/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/init(named:))*