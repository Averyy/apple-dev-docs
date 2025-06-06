# prepare(for:sender:)

**Framework**: AppKit  
**Kind**: method

Called when a segue is about to be performed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func prepare(for segue: NSStoryboardSegue, sender: Any?)
```

#### Discussion

The default implementation of this method does nothing; you can override it to pass relevant data to the new view controller or window controller, based on the context of the segue. The `segue` object describes the transition and includes references to both controllers involved in the segue.

Segues can be triggered from multiple sources, so use the information in the `segue` and `sender` parameters to disambiguate between different logical paths in your app. For example, if the segue originated from a table view, the `sender` parameter would identify the cell that the user clicked. You could use that information to set the data on the destination view controller.

## Parameters

- `segue`: The segue object containing information about the view controllers involved in the segue.
- `sender`: The object that initiated the segue. You might use this parameter to perform different actions based on which control (or other object) initiated the segue.

## See Also

- [func performSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?)](nssegueperforming/performsegue(withidentifier:sender:).md)
  Performs the specified segue.
- [func shouldPerformSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?) -> Bool](nssegueperforming/shouldperformsegue(withidentifier:sender:).md)
  Called immediately prior to the performance of a storyboard segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegueperforming/prepare(for:sender:))*