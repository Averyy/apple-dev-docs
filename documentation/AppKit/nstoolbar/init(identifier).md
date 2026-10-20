# init(identifier:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a newly allocated toolbar with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
init(identifier: NSToolbar.Identifier)
```

```objc
- (instancetype) initWithIdentifier:(NSToolbarIdentifier) identifier;
```

#### Return Value

The initialized toolbar object.

#### Discussion

`identifier` is never seen by users and should not be localized. See the [`identifier`](./identifier-swift.property.md) property for important information.

## Parameters

- `identifier`: A string used by the class to identify the kind of the toolbar.

## See Also

### Related Documentation
- [var identifier: NSToolbar.Identifier](./identifier-swift.property.md)
  The value you use to identify the toolbar in your app.
### Creating an toolbar object
- [convenience init()](./init%28%29.md)
  Creates a new toolbar with an empty identifier string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/init(identifier:))*