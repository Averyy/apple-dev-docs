# maxOutputLength

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The maximum length of output APDU (Application Protocol Data Unit) that the Smart Card reader slot is able to transfer from the Smart Card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var maxOutputLength: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger maxOutputLength;
```

## See Also

### Getting the Slot Configuration
- [var name: String](./name.md)
  The name of the Smart Card reader slot.
- [var maxInputLength: Int](./maxinputlength.md)
  The maximum length of input APDU (Application Protocol Data Unit) that the Smart Card reader slot is able to transfer to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/maxoutputlength)*