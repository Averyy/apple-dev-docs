# performSegue(withIdentifier:sender:)

**Framework**: AppKit  
**Kind**: method

Performs the specified segue.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func performSegue(withIdentifier identifier: NSStoryboardSegue.Identifier, sender: Any?)
```

#### Discussion

Apps typically do not need to trigger segues programmatically. If needed, you can call this method to trigger a segue for an action that cannot be expressed in a storyboard file, such as a transition between scenes in different storyboards.

Typically, a segue is triggered by a user action, such as clicking a button. In Interface Builder, configure an object, such as a control embedded in the view controller’s view hierarchy, to trigger the segue.

## Parameters

- `identifier`: In Interface Builder, you can provide an identifier string to a segue using the inspector. Pass this string to this parameter.
- `sender`: The object that you want to use to initiate the segue. This parameter makes the object available to your implementation during the segue.

## See Also

- [func prepare(for: NSStoryboardSegue, sender: Any?)](nssegueperforming/prepare(for:sender:).md)
  Called when a segue is about to be performed.
- [func shouldPerformSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?) -> Bool](nssegueperforming/shouldperformsegue(withidentifier:sender:).md)
  Called immediately prior to the performance of a storyboard segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegueperforming/performsegue(withidentifier:sender:))*