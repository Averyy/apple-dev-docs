# writingToolsCoordinator(_:requestsRangeInContextWithIdentifierFor:completion:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to provide the location of the character at the specified point in your view’s coordinate system.

**Availability**:
- macOS 15.2+ - Deprecated in 15.4

> **Deprecated**: In macOS 15.4 and later, NSWritingToolsCoordinator automatically determines the location of the character at the specified point in your view's coordinate system and no longer calls this method.

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, requestsRangeInContextWithIdentifierFor point: NSPoint, completion: @escaping @Sendable (NSRange, UUID) -> Void)
```

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, rangeInContextWithIdentifierFor point: NSPoint) async -> (NSRange, UUID)
```

```objc
- (void) writingToolsCoordinator:(NSWritingToolsCoordinator *) writingToolsCoordinator requestsRangeInContextWithIdentifierForPoint:(NSPoint) point completion:(void (^)(NSRange range, NSUUID *contextID)) completion;
```

## Discussion

When someone interacts with your view during a proofreading operation, Writing Tools calls this method to get the location of the interaction. If the interaction occurs in the text of one of your [`NSWritingToolsCoordinator.Context`](../context.md) objects, configure an [`NSRange`](../../../Foundation/nsrange-c.struct.md) with the character’s location in that context object and a length of `1`. If the interaction occurs outside of the text of your context objects, configure the range with a location of `NSNotFound`.

When specifying the location of a character in your context object, provide a location relative to the start of your context object’s text. The first character in a context object’s text is always at location `0`, and it’s your responsibility to track the location of the context object’s text in your text storage object. When the context object’s text begins in the middle of your text storage, subtract the starting location of the context object’s text from the location you specify in your range value. For example, if the context object’s text starts at character `100` in your text storage, and an interaction occurs with the character at location `102`, specify a range with a location of `2` and a length of `1`.

## Parameters

- `writingToolsCoordinator`: The coordinator object requesting information from your custom view.
- `point`: A point in your view’s coordinate space. Find the location of the text under this point, if any.
- `completion`: A handler to execute with the required information. This handler has no return value and takes an [`NSRange`](../../../Foundation/nsrange-c.struct.md) and [`UUID`](../../../Foundation/uuid.md) as parameters. Set the range to the character’s location in one of your [`NSWritingToolsCoordinator.Context`](../context.md) objects, which you specify using the [`UUID`](../../../Foundation/uuid.md) parameter. You must call this handler at some point during your method’s implementation.

## See Also

### Displaying proofreading marks
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsBoundingBezierPathsFor: NSRange, in: NSWritingToolsCoordinator.Context, completion: ([NSBezierPath]) -> Void)](./writingtoolscoordinator%28_,requestsboundingbezierpathsfor,in,completion%29.md)
  Asks the delegate to provide the bounding paths for the specified text in your view.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsUnderlinePathsFor: NSRange, in: NSWritingToolsCoordinator.Context, completion: ([NSBezierPath]) -> Void)](./writingtoolscoordinator%28_,requestsunderlinepathsfor,in,completion%29.md)
  Asks the delegate to provide an underline shape for the specified text during a proofreading session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsrangeincontextwithidentifierfor:completion:))*