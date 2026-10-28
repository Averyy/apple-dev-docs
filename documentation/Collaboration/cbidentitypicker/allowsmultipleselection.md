# allowsMultipleSelection

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the user is allowed to select multiple identities.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var allowsMultipleSelection: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL allowsMultipleSelection;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the user can select multiple records; otherwise, [`false`](../../Swift/false.md). The default value is [`false`](../../Swift/false.md).

## See Also

### Setting and Getting Properties
- [var title: String?](./title.md)
  The title of the identity picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentitypicker/allowsmultipleselection)*