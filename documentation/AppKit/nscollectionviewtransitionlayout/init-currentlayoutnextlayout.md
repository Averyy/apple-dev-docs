# init(currentLayout:nextLayout:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns the transition layout object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
init(currentLayout: NSCollectionViewLayout, nextLayout newLayout: NSCollectionViewLayout)
```

#### Return Value

An initialized transition layout or `nil` if the object could not be initialized.

#### Discussion

This method initializes the transition layout object and saves references to the current and new layout objects. If you subclass and implement your own initialization method, you must call this method to initialize the superclass.

## Parameters

- `currentLayout`: The layout object currently in use by the collection view.
- `newLayout`: The new layout object that is about to be installed into the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/init(currentlayout:nextlayout:))*