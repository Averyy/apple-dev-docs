# initWithTitle:lowerBound:upperBound:gridlinePositions:valueDescriptionProvider:

**Framework**: Accessibility  
**Kind**: method  
**Role**: Instance Method

Creates a numeric data axis with the specified title, lower bound value, upper bound value, gridline positions, and value description provider block.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (instancetype) initWithTitle:(NSString *) title lowerBound:(double) lowerbound upperBound:(double) upperBound gridlinePositions:(NSArray<NSNumber *> *) gridlinePositions valueDescriptionProvider:(NSString * (^)(double )) valueDescriptionProvider;
```

## See Also

### Creating a numeric data axis
- [- initWithAttributedTitle:lowerBound:upperBound:gridlinePositions:valueDescriptionProvider:](./initwithattributedtitle_lowerbound_upperbound_gridlinepositions_valuedescriptionprovider_.md)
  Creates a numeric data axis with the specified attributed title, lower bound value, upper bound value, gridline positions, and value description provider block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axnumericdataaxisdescriptor/initwithtitle:lowerbound:upperbound:gridlinepositions:valuedescriptionprovider:)*