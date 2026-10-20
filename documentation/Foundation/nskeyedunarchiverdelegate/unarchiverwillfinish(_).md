# unarchiverWillFinish(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that decoding is about to finish.

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
optional func unarchiverWillFinish(_ unarchiver: NSKeyedUnarchiver)
```

```objc
- (void) unarchiverWillFinish:(NSKeyedUnarchiver *) unarchiver;
```

## Parameters

- `unarchiver`: An unarchiver for which the receiver is the delegate.

## See Also

### Finishing Decoding
- [func unarchiverDidFinish(NSKeyedUnarchiver)](./unarchiverdidfinish%28_%29.md)
  Notifies the delegate that decoding has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiverwillfinish(_:))*