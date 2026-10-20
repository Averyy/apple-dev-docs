# unarchiverDidFinish(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that decoding has finished.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func unarchiverDidFinish(_ unarchiver: NSKeyedUnarchiver)
```

```objc
- (void) unarchiverDidFinish:(NSKeyedUnarchiver *) unarchiver;
```

## Parameters

- `unarchiver`: An unarchiver for which the receiver is the delegate.

## See Also

### Finishing Decoding
- [func unarchiverWillFinish(NSKeyedUnarchiver)](./unarchiverwillfinish%28_%29.md)
  Notifies the delegate that decoding is about to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiverdidfinish(_:))*