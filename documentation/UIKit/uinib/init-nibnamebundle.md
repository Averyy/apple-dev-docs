# init(nibName:bundle:)

**Framework**: UIKit  
**Kind**: init

Returns a nib object from the nib file in the specified bundle.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(nibName name: String, bundle bundleOrNil: Bundle?)
```

#### Return Value

The initialized [`UINib`](uinib.md) object. An exception is thrown if there were errors during initialization or the nib file could not be located.

#### Discussion

The [`UINib`](uinib.md) object looks for the nib file in the bundle’s language-specific project directories first, followed by the `Resources` directory.

## Parameters

- `name`: The name of the nib file, without any leading path information.
- `bundleOrNil`: The bundle in which to search for the nib file. If you specify  , this method looks for the nib file in the main bundle.

## See Also

- [init(data: Data, bundle: Bundle?)](uinib/init(data:bundle:).md)
  Creates a nib object from nib data stored in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinib/init(nibname:bundle:))*