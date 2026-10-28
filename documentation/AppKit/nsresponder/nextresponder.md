# nextResponder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The next responder after this one, or `nil` if it has none.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var nextResponder: NSResponder? { get set }
```

```objc
@property (unsafe_unretained, nullable) NSResponder * nextResponder;
```

## Discussion

The next responder must be an object that inherits, directly or indirectly, from `NSResponder`.

## See Also

### Related Documentation
- [func noResponder(for: Selector)](./noresponder%28for%29.md)
  Handles the case where an event or action message falls off the end of the responder chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/nextresponder)*