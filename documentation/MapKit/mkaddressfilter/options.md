# MKAddressFilter.Options

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

A structure that contains options for filtering results in a search.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Options
```

```c
enum MKAddressFilterOption : NSUInteger;
```

## Topics

### Creating a filter result
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
  Creates a filter options object.
### Getting search filter options
- [static var administrativeArea: MKAddressFilter.Options](./options/administrativearea.md)
  The primary administrative divisions of countries or regions.
- [static var country: MKAddressFilter.Options](./options/country.md)
  Countries and regions.
- [static var locality: MKAddressFilter.Options](./options/locality.md)
  Local administrative divisions, postal cities, and populated places.
- [static var postalCode: MKAddressFilter.Options](./options/postalcode.md)
  An address code for mail sorting and delivery.
- [static var subAdministrativeArea: MKAddressFilter.Options](./options/subadministrativearea.md)
  The secondary administrative divisions of countries or regions.
- [static var subLocality: MKAddressFilter.Options](./options/sublocality.md)
  Local administrative subdivisions, postal city subdistricts, and neighborhoods.
- [static var administrativeArea: MKAddressFilter.Options](./options/administrativearea.md)
  The primary administrative divisions of countries or regions.
- [static var country: MKAddressFilter.Options](./options/country.md)
  Countries and regions.
- [static var locality: MKAddressFilter.Options](./options/locality.md)
  Local administrative divisions, postal cities, and populated places.
- [static var postalCode: MKAddressFilter.Options](./options/postalcode.md)
  An address code for mail sorting and delivery.
- [static var subAdministrativeArea: MKAddressFilter.Options](./options/subadministrativearea.md)
  The secondary administrative divisions of countries or regions.
- [static var subLocality: MKAddressFilter.Options](./options/sublocality.md)
  Local administrative subdivisions, postal city subdistricts, and neighborhoods.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Local search
- [Interacting with nearby points of interest](../interacting-with-nearby-points-of-interest.md)
  Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [enum MKLocalSearchRegionPriority](../mklocalsearchregionpriority.md)
  A value that indicates the importance of the configured region.
- [MKLocalSearch.ResultType](../mklocalsearch/resulttype.md)
  Options that indicate types of search results.
- [class MKLocalSearch](../mklocalsearch.md)
  A utility object for initiating map-based searches and processing the results.
- [class MKAddressFilter](../mkaddressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [MKLocalSearchCompleter.ResultType](../mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.
- [class MKLocalSearchCompleter](../mklocalsearchcompleter.md)
  A utility object for generating a list of completion strings based on a partial search string that you provide.
- [class MKLocalSearchCompletion](../mklocalsearchcompletion.md)
  A fully formed string that completes a partial string.
- [class MKLocalPointsOfInterestRequest](../mklocalpointsofinterestrequest.md)
  A structured request to use when searching for points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressfilter/options)*