# init(nibName:bundle:)

**Framework**: AppKit  
**Kind**: init

Returns a view controller object initialized to the nib file in the specified bundle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
init(nibName nibNameOrNil: NSNib.Name?, bundle nibBundleOrNil: Bundle?)
```

#### Return Value

The initialized [`NSViewController`](nsviewcontroller.md) object.

#### Discussion

The [`NSViewController`](nsviewcontroller.md) object looks for the nib file in the bundle’s language-specific project directories first, followed by the Resources directory.

The specified nib file should typically have the class of the file’s owner set to [`NSViewController`](nsviewcontroller.md), or a custom subclass, with the `view` outlet connected to a view.

If you pass in `nil` for `nibNameOrNil`, [`nibName`](nsviewcontroller/nibname.md) returns `nil` and [`loadView()`](nsviewcontroller/loadview().md) throws an exception; in this case you must set [`view`](nsviewcontroller/view.md) before [`view`](nsviewcontroller/view.md) is invoked, or override [`loadView()`](nsviewcontroller/loadview().md).

## Parameters

- `nibNameOrNil`: The name of the nib file, without any leading path information.
- `nibBundleOrNil`: The bundle in which to search for the nib file. If you specify  , this method looks for the nib file in the main bundle.

## See Also

- [func loadView()](nsviewcontroller/loadview.md)
  Instantiates a view from a nib file and sets the value of the [`view`](nsviewcontroller/view.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/init(nibname:bundle:))*