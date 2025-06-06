# init(completion:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a search request based on the specified search completion data.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
init(completion: MKLocalSearchCompletion)
```

#### Return Value

An initialized search request.

#### Discussion

Use this method when initializing your object from [`MKLocalSearchCompleter`](mklocalsearchcompleter.md) objects. You don’t need to use this method if you intend to provide the search string and region information yourself.

## Parameters

- `completion`: A search completion object that MapKit obtains from an   object. The search request uses the provided object to set the value of the   property.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [init()](mklocalsearch/request/init.md)
  Creates a local search request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/request/init(completion:))*