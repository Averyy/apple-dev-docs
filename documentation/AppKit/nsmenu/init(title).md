# init(title:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a menu having the specified title and with autoenabling of menu items turned on.

**Availability**:
- macOS

## Declaration

```swift
init(title: String)
```

```objc
- (instancetype) initWithTitle:(NSString *) title;
```

## Return Value

The initialized `NSMenu` object or `nil` if the object could not be initialized.

## Discussion

This method is the designated initializer for the class.

## Parameters

- `title`: The title to assign to the menu.

## See Also

### Related Documentation
- [var autoenablesItems: Bool](./autoenablesitems.md)
  Indicates whether the menu automatically enables and disables its menu items.
### Creating an NSMenu Object
- [init(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/init(title:))*