# shouldPerformSegue(withIdentifier:sender:)

**Framework**: AppKit  
**Kind**: method

Called immediately prior to the performance of a storyboard segue.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func shouldPerformSegue(withIdentifier identifier: NSStoryboardSegue.Identifier, sender: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow a segue to proceed or [`false`](https://developer.apple.com/documentation/Swift/false) to stop it from proceeding.

#### Discussion

Override this method to return [`false`](https://developer.apple.com/documentation/Swift/false) for cases where you want to prevent the performance of a segue. By default, invocation of a segue results in the segue being performed.

## Parameters

- `identifier`: Using the Interface Builder inspector, provide a unique identifier string for each segue in a storyboard. The system provides a segue’s identifier to this parameter when it calls this method. The identifier string is used to locate the segue inside the storyboard file that contains the view controller.
- `sender`: The object that initiated the segue. This object is made available for informational purposes during the segue.

## See Also

- [func performSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?)](nssegueperforming/performsegue(withidentifier:sender:).md)
  Performs the specified segue.
- [func prepare(for: NSStoryboardSegue, sender: Any?)](nssegueperforming/prepare(for:sender:).md)
  Called when a segue is about to be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegueperforming/shouldperformsegue(withidentifier:sender:))*