# region

**Framework**: MapKit JS  
**Kind**: property

A map region that provides a hint about the geographic area to search.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get region(): CoordinateRegion | null;
set region(value: CoordinateRegion | null);
```

#### Discussion

This property specifies a region of a map in which to search. In a map application, this is typically the region the map displays.

```javascript
{ region: map.region }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/region)*