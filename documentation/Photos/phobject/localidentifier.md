# localIdentifier

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A unique string that persistently identifies the object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var localIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * localIdentifier;
```

## Mentions

- [Requesting Changes to the Photo Library](../../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Discussion

Use this string to find the object by using the [`fetchAssets(withLocalIdentifiers:options:)`](../phasset/fetchassets%28withlocalidentifiers,options%29.md), [`fetchAssetCollections(withLocalIdentifiers:options:)`](../phassetcollection/fetchassetcollections%28withlocalidentifiers,options%29.md), or [`fetchCollectionLists(withLocalIdentifiers:options:)`](../phcollectionlist/fetchcollectionlists%28withlocalidentifiers,options%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phobject/localidentifier)*