# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Specifies the delegate of the sharing service.

**Availability**:
- macOS 10.8+

## Declaration

```swift
weak var delegate: (any NSSharingServiceDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSSharingServiceDelegate> delegate;
```

#### Discussion

The delegate class must conform to the [`NSSharingServiceDelegate`](../nssharingservicedelegate.md) protocol.

## See Also

### Managing the Delegate
- [protocol NSSharingServiceDelegate](../nssharingservicedelegate.md)
  A set of methods that you use to customize the position and animation of a share sheet, and to be notified whether the item is successfully shared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/delegate)*