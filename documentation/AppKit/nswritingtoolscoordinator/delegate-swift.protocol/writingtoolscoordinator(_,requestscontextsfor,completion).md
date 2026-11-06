# writingToolsCoordinator(_:requestsContextsFor:completion:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks your delegate to provide the text to evaluate during the Writing Tools operation.

**Availability**:
- macOS 15.2+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, requestsContextsFor scope: NSWritingToolsCoordinator.ContextScope, completion: @escaping @Sendable ([NSWritingToolsCoordinator.Context]) -> Void)
```

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, contextsFor scope: NSWritingToolsCoordinator.ContextScope) async -> [NSWritingToolsCoordinator.Context]
```

```objc
- (void) writingToolsCoordinator:(NSWritingToolsCoordinator *) writingToolsCoordinator requestsContextsForScope:(NSWritingToolsCoordinatorContextScope) scope completion:(void (^)(NSArray<NSWritingToolsCoordinatorContext *> *)) completion;
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](../../adding-writing-tools-support-to-a-custom-nsview.md)

## Discussion

At the start of every operation, the [`NSWritingToolsCoordinator`](../../nswritingtoolscoordinator.md) object calls this method to request the text to evaluate. Use this method to create one or more [`NSWritingToolsCoordinator.Context`](../context.md) objects with your view’s text. Create only one [`NSWritingToolsCoordinator.Context`](../context.md) object if your view has only one text storage object. If your view contains multiple text storage objects, create separate [`NSWritingToolsCoordinator.Context`](../context.md) objects for each text storage object. Writing Tools returns updates for each context object separately, making it easier for you to incorporate changes into the correct text storage object. Don’t create multiple context objects if your view has only one text storage object.

The `scope` parameter tells you what content Writing Tools expects you to provide in your context object. For example, Writing Tools expects you to provide the selected text when the parameter contains the [`NSWritingToolsCoordinator.ContextScope.userSelection`](../contextscope/userselection.md) option. When Writing Tools requests a subset of your overall text, include some of the surrounding text in your context object too. Writing Tools can use the extra text you provide to improve the results of its evaluation. For example, it might use an entire paragraph, instead of only the selected sentence, to evaluate ways to rewrite that sentence. It’s best to include the text up to the nearest paragraph boundary before and after the selection. If you include extra text in your context object, set the [`range`](../context/range.md) property to the range of the selected text.

> **Note**: When a context object stores only a subset of your view’s text, record additional information to map the location of that text to the correct location in your view’s text storage. Keep that information up-to-date throughout the Writing Tools session.

Pass the context objects you create to the provided completion handler before your method returns. Writing Tools waits for you to call the completion handler before proceeding with the operation.

### Subclassing a system text view

`NSTextView` implements this method for you. If you subclass it, call the superclass implementation and pass along the context objects it provides. You don’t create those objects, so you can’t choose their text directly — the superclass builds each one from your text storage.

> ❗ **Important**: Don’t replace the context objects the superclass provides with your own. Each [`NSWritingToolsCoordinator.Context`](../context.md) object has a unique identifier, and the superclass keeps referring to the object it created — including when it reports typing and undo to the coordinator during the session. Substituting a different object leaves the two out of sync: those reports are silently discarded, Writing Tools continues from a stale idea of your text, and the results it applies when the session ends can replace or delete text beyond the range you intended.

Because the superclass builds each context object from your text storage, attributes already on your storage are carried into the context. Use that to describe structure your text storage doesn’t otherwise express: add `NSPresentationIntentAttributeName` and `NSInlinePresentationIntentAttributeName` to your storage, and include `NSWritingToolsResultPresentationIntent` in your view’s `allowedWritingToolsResultOptions`.

## Parameters

- `writingToolsCoordinator`: The coordinator object requesting information from your custom view.
- `scope`: The amount of text the coordinator requested. Use this property to determine if Writing Tools is evaluating all of your text or only a subset.
- `completion`: A completion block to execute with the required information. You must execute this block once at end of your method’s implementation. The block has no return value and takes an array of [`NSWritingToolsCoordinator.Context`](../context.md) objects that contain the requested information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestscontextsfor:completion:))*