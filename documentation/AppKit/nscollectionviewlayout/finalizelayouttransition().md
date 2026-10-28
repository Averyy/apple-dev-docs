# finalizeLayoutTransition()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs any final steps related to a layout transition before the transition animations actually occur.

**Availability**:
- macOS

## Declaration

```swift
func finalizeLayoutTransition()
```

```objc
- (void) finalizeLayoutTransition;
```

## Discussion

After it has gathered all of the layout attributes it needs, the collection view calls this method on both the new and old layout objects to give them time to perform any additional operations. Use this method to clean up any data structures or caches related to the transition that your layout object no longer needs.

## See Also

### Transitioning Between Layouts
- [func prepareForTransition(from: NSCollectionViewLayout)](./preparefortransition%28from%29.md)
  Prepares the layout object to be installed in the collection view.
- [func prepareForTransition(to: NSCollectionViewLayout)](./preparefortransition%28to%29.md)
  Prepares the layout object to be uninstalled from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/finalizelayouttransition())*