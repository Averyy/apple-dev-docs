# init(data:bundle:)

**Framework**: UIKit  
**Kind**: init

Creates a nib object from nib data stored in memory.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(data: Data, bundle bundleOrNil: Bundle?)
```

#### Return Value

The initialized [`UINib`](uinib.md) object. An exception is thrown if there were errors during initialization or the nib data could not be located.

#### Discussion

The [`UINib`](uinib.md) object looks for the nib file in the bundle’s language-specific project directories first, followed by the `Resources` directory.

The preferred mechanism for instantiating [`UINib`](uinib.md) objects is with [`init(nibName:bundle:)`](uinib/init(nibname:bundle:).md). A [`UINib`](uinib.md) object instantiated using [`init(data:bundle:)`](uinib/init(data:bundle:).md) can’t release the cached data under low memory conditions. Your app should prepare to release the [`UINib`](uinib.md) object and the data under low memory conditions, recreating both the next time the app needs to instantiate the nib.

## Parameters

- `data`: A block of memory that contains nib data.
- `bundleOrNil`: The bundle in which to search for resources referenced by the nib. If you specify  , this method looks for the nib file in the main bundle.

## See Also

- [init(nibName: String, bundle: Bundle?)](uinib/init(nibname:bundle:).md)
  Returns a nib object from the nib file in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinib/init(data:bundle:))*