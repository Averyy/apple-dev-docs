# queryFragment

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The search string that you want completions for.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var queryFragment: String { get set }
```

```objc
@property (nonatomic, copy) NSString * queryFragment;
```

#### Discussion

Assigning a string to this property initiates a search based on that string. The completer object waits a short amount of time before initiating new searches. This delay gives you enough time to update the search string based on typed input from the user. For example, if you’re using a text field to manage the input from the user, use the [`textField(_:shouldChangeCharactersIn:replacementString:)`](../../UIKit/uitextfielddelegate/textfield%28_,shouldchangecharactersin,replacementstring%29.md) method of the text field’s delegate to update the value of this property, as the following example shows:

```objc
- (BOOL)textField:(UITextField *)textField shouldChangeCharactersInRange:(NSRange)range
         replacementString:(NSString *)string {
    self.completer.queryFragment = textField.text;
 
    return YES;
}
```

## See Also

### Specifying the query attributes
- [var addressFilter: MKAddressFilter?](./addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var region: MKCoordinateRegion](./region.md)
  The region that defines the geographic scope of the search.
- [var regionPriority: MKLocalSearchRegionPriority](./regionpriority.md)
  A value that indicates the importance of the configured region.
- [var resultTypes: MKLocalSearchCompleter.ResultType](./resulttypes.md)
  The types of search completions to include.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./pointofinterestfilter.md)
  A filter that lists point of interest categories to include or exclude in the search.
- [var filterType: MKLocalSearchCompleter.FilterType](./filtertype-swift.property.md)
  The filter options for the search results.
- [MKLocalSearchCompleter.FilterType](./filtertype-swift.enum.md)
  Constants indicating the types of search completions to return.
- [MKLocalSearchCompleter.ResultType](./resulttype.md)
  Options that indicate types of search completions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/queryfragment)*