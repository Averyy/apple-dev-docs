# layoutManager(_:shouldUseTemporaryAttributes:forDrawingToScreen:atCharacterIndex:effectiveRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to use temporary attributes when drawing the text.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldUseTemporaryAttributes attrs: [NSAttributedString.Key : Any] = [:], forDrawingToScreen toScreen: Bool, atCharacterIndex charIndex: Int, effectiveRange effectiveCharRange: NSRangePointer?) -> [NSAttributedString.Key : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) layoutManager:(NSLayoutManager *) layoutManager shouldUseTemporaryAttributes:(NSDictionary<NSString *,id> *) attrs forDrawingToScreen:(BOOL) toScreen atCharacterIndex:(NSUInteger) charIndex effectiveRange:(NSRangePointer) effectiveCharRange;
```

## Return Value

The temporary attributes for the layout manager to use, or `nil` if no temporary attributes are to be used.

## Discussion

The default behavior, if this method is not implemented, is to use temporary attributes only when drawing to the screen, so an implementation to match that behavior would return `attrs` if `toScreen` is [`true`](../../Swift/true.md) and `nil` otherwise, without changing `effectiveCharRange`.

## Parameters

- `layoutManager`: The layout manager sending the message.
- `attrs`: The temporary attributes currently in effect for the given character range.
- `toScreen`: [`true`](../../Swift/true.md) if the layout manager is drawing to the screen; otherwise, [`false`](../../Swift/false.md).
- `charIndex`: Index of the first character in the range being drawn.
- `effectiveCharRange`: On input and output, the effective range to which the temporary attributes apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:shouldusetemporaryattributes:fordrawingtoscreen:atcharacterindex:effectiverange:))*