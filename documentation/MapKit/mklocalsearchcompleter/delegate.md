# delegate

**Framework**: MapKit  
**Kind**: property

The object that receives the completion results.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any MKLocalSearchCompleterDelegate)? { get set }
```

#### Discussion

You must provide a delegate object to receive completion results and to handle any errors that might occur. For more information about the methods of the delegate protocol, see [`MKLocalSearchCompleterDelegate`](mklocalsearchcompleterdelegate.md).

## See Also

- [protocol MKLocalSearchCompleterDelegate](mklocalsearchcompleterdelegate.md)
  Methods the delegate calls with search completion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/delegate)*