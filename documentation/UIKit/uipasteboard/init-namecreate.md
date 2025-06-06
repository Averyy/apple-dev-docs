# init(name:create:)

**Framework**: UIKit  
**Kind**: init

Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init?(name pasteboardName: UIPasteboard.Name, create: Bool)
```

#### Return Value

A pasteboard object you can use to transfer data within an app or between apps that have the same team ID.

#### Discussion

Call this method to create custom app pasteboards. (You can also use it to obtain the general pasteboard, but the [`general`](uipasteboard/general.md) class method exists for that purpose.) App pasteboards this method returns aren’t persistent, existing only until the app quits. Starting in iOS 10, persistent, named pasteboards are deprecated. Instead, use a shared container, as described in the overview for the [`UIPasteboard`](uipasteboard.md) class.

## Parameters

- `pasteboardName`: A string or string constant that identifies (or should identify) the pasteboard. To create a pasteboard with a   name, specify a   value for this parameter.
- `create`: A Boolean value that specifies whether to create the pasteboard if it doesn’t already exist. Specify   for system pasteboards or if you want to use an existing app pasteboard.

## See Also

- [class var general: UIPasteboard](uipasteboard/general.md)
  The systemwide general pasteboard, which you use for general copy-paste operations.
- [class func withUniqueName() -> UIPasteboard](uipasteboard/withuniquename.md)
  Returns an app pasteboard that you identify by a unique system-generated name.
- [class func remove(withName: UIPasteboard.Name)](uipasteboard/remove(withname:).md)
  Invalidates the designated app pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/init(name:create:))*