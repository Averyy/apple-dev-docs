# deleteDrawable()

**Framework**: GLKit  
**Kind**: method

Deletes the drawable object associated with the view.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func deleteDrawable()
```

#### Discussion

The drawable object consumes a significant amount of memory, so whenever the view is not going to be used to display content for a significant period of time, your application should call this method to dispose of the underlying memory. For example, your application might call this method after hiding a view or before transitioning to another screen of content.

If you use a [`GLKViewController`](glkviewcontroller.md) object to manage the view, the view controller automatically calls this method whenever your application moves into the background.

After calling this method, do not invalidate the view’s contents or call the view’s [`display()`](glkview/display().md) method until you are ready to display the content again to the user; drawing the view’s contents automatically reallocates the drawable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/deletedrawable())*