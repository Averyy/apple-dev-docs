# validateVisibleItems()

**Framework**: AppKit  
**Kind**: method

Validates the toolbar’s visible items during a window update.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateVisibleItems()
```

#### Discussion

Typically, you override this method and use it to customize the validation process. The default implementation calls the [`validate()`](nstoolbaritem/validate().md) method of each visible item in the toolbar, including items that have their [`autovalidates`](nstoolbaritem/autovalidates.md) property set to [`false`](https://developer.apple.com/documentation/Swift/false). If you override this method, call `super` at some point during your implementation.

The toolbar doesn’t validate its content for some events, including [`NSLeftMouseDragged`](nsleftmousedragged.md), [`NSRightMouseDragged`](nsrightmousedragged.md), [`NSOtherMouseDragged`](nsothermousedragged.md), [`NSMouseEntered`](nsmouseentered.md), [`NSMouseExited`](nsmouseexited.md), [`NSScrollWheel`](nsscrollwheel.md), [`NSCursorUpdate`](nscursorupdate.md), [`NSKeyDown`](nskeydown.md). In addition, the toolbar defers validation for [`NSKeyUp`](nskeyup.md) and [`NSFlagsChanged`](nsflagschanged.md) events until a pause of 0.85 seconds occurs or the window processes an event other than [`NSKeyUp`](nskeyup.md) or [`NSFlagsChanged`](nsflagschanged.md). So a rapid sequence of key events doesn’t trigger any validation.

To trigger validation for all toolbars, call the app’s [`setWindowsNeedUpdate(_:)`](nsapplication/setwindowsneedupdate(_:).md) method with a value of [`true`](https://developer.apple.com/documentation/Swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/validatevisibleitems())*