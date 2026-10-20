# init(named:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates an appearance object based on the name of one of the standard system appearances.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init?(named name: NSAppearance.Name)
```

```objc
+ (NSAppearance *) appearanceNamed:(NSAppearanceName) name;
```

#### Return Value

A standard [`NSAppearance`](../nsappearance.md) object.

#### Discussion

When you specify a standard appearance name—such as [`aqua`](./name-swift.struct/aqua.md)—this method returns a built-in appearance.

## Parameters

- `name`: The name of a standard appearance. See [`NSAppearance.Name`](./name-swift.struct.md) for the list of standard appearance names.

## See Also

### Creating an Appearance
- [init?(appearanceNamed: NSAppearance.Name, bundle: Bundle?)](./init%28appearancenamed,bundle%29.md)
  Creates an appearance object from the named appearance file located in the specified bundle.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/init(named:))*