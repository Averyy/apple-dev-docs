# init(identifiers:classifyingLabels:)

**Framework**: AVFoundation  
**Kind**: init

Creates a metadata collector to access a stream’s metadata groups matching the specified array of identifiers and classifying labels.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.3+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.3+

## Declaration

```swift
init(identifiers: [String]?, classifyingLabels: [String]?)
```

#### Return Value

An instance of `AVPlayerItemMetadataCollector`.

#### Discussion

You can use the `identifiers` and `classifyingLabels` arguments to configure the metadata collector to filter its output to only the metadata items matching the specified criteria.

You use the `identifiers` argument to filter the output to a particular set of metadata identifiers. For instance, if the stream’s `#EXT-X-DATERANGE` tags define multiple metadata attributes, but you are only interested in the values for the `X-AD-ID` and `X-AD-URL` attributes, you could configure the collector as follows:

The `classifyingLabels` argument is used to filter by the `#EXT-X-DATERANGE` tag’s `CLASS` attribute. The `CLASS` attribute can be used to define a set of attribute/value pairs for a particular purpose (such as describing an ad) and then mark each `#EXT-X-DATERANGE` instance as having those semantics. For instance, this might be used by a third party advertising SDK to filter the output to only the metadata relevant to its needs. It could define an “Advertiser-ad” `CLASS` with the following attributes:

- `X-ADVERTISER-AD-GUID` (the unique identifier for the ad)
- `X-ADVERTISER-AD-AGE` (the number of days in its inventory)

The SDK could require clients to pass it any player items the app creates so it could configure them to output its needed data as shown below:

## Parameters

- `identifiers`: An optional array of metadata identifiers indicating the metadata items that the output should provide.
- `classifyingLabels`: A optional array of classifying labels indicating the metadata items that the output should provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/init(identifiers:classifyinglabels:))*