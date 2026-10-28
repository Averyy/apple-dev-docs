# shouldPerformSegue(withIdentifier:sender:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called immediately prior to the performance of a storyboard segue.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func shouldPerformSegue(withIdentifier identifier: NSStoryboardSegue.Identifier, sender: Any?) -> Bool
```

```objc
- (BOOL) shouldPerformSegueWithIdentifier:(NSStoryboardSegueIdentifier) identifier sender:(id) sender;
```

## Return Value

[`true`](../../Swift/true.md) to allow a segue to proceed or [`false`](../../Swift/false.md) to stop it from proceeding.

## Discussion

Override this method to return [`false`](../../Swift/false.md) for cases where you want to prevent the performance of a segue. By default, invocation of a segue results in the segue being performed.

## Parameters

- `identifier`: The string that identifies the segue to be performed.

  Using the Interface Builder inspector, provide a unique identifier string for each segue in a storyboard. The system provides a segue’s identifier to this parameter when it calls this method. The identifier string is used to locate the segue inside the storyboard file that contains the view controller.

  > **Note**:  This method throws an [Exception handling](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18) if there is no segue with the specified identifier.
- `sender`: The object that initiated the segue. This object is made available for informational purposes during the segue.

## See Also

### Working with Storyboard Segues
- [func performSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?)](./performsegue%28withidentifier,sender%29.md)
  Performs the specified segue.
- [func prepare(for: NSStoryboardSegue, sender: Any?)](./prepare%28for,sender%29.md)
  Called when a segue is about to be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegueperforming/shouldperformsegue(withidentifier:sender:))*