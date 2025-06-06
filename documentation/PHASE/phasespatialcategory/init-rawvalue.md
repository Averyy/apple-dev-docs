# init(rawValue:)

**Framework**: PHASE  
**Kind**: init

Initializes a spatial category with the given string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

To initialize a spatial category:

```swift
// Set the raw-value variable to the `directPathTransmission` constant. 
var rawValue: String = PHASESpatialCategoryDirectPathTransmission
var spatialPipelineOption = PHASESpatialCategory(rawValue: rawValue)
```

To check a spatial category’s raw value, see the Objective-C declaration of the struct member.

## Parameters

- `rawValue`: The enumeration case’s underlying string value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialcategory/init(rawvalue:))*