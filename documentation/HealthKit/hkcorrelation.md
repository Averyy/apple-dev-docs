# HKCorrelation

**Framework**: HealthKit  
**Kind**: class

A sample that groups multiple related samples into a single entry.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKCorrelation
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)
- [Saving data to HealthKit](saving-data-to-healthkit.md)

#### Overview

HealthKit uses correlations to represent both blood pressure and food.

- Blood pressure correlations always include two quantity samples, representing the systolic and diastolic values.
- Food correlations can contain a wide range of dietary information about the food, including information about the fat, protein, carbohydrates, energy, and vitamins consumed.

In general, a food correlation should include at least a [`dietaryEnergyConsumed`](hkquantitytypeidentifier/dietaryenergyconsumed.md) sample. You can also add nutritional quantity samples for any other items you want to track. Use the [`HKMetadataKeyFoodType`](hkmetadatakeyfoodtype.md) key to indicate the food’s name.

The [`HKCorrelation`](hkcorrelation.md) class is a concrete subclass of the [`HKSample`](hksample.md) class. Correlations are immutable: You set the correlation’s properties when the object is first created, and they cannot change.

##### Extend Correlation Samples

Like many HealthKit classes, the `HKCorrelation` class should not be subclassed. You can extend the correlation class by adding metadata with custom keys as appropriate for your app.

For more information, see the [`init(type:start:end:objects:metadata:)`](hkcorrelation/init(type:start:end:objects:metadata:).md) method.

## Topics

### Creating Correlations
- [convenience init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>)](hkcorrelation/init(type:start:end:objects:).md)
  Instantiates and returns a new correlation instance.
- [convenience init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>, metadata: [String : Any]?)](hkcorrelation/init(type:start:end:objects:metadata:).md)
  Instantiates and returns a new correlation instance with the provided metadata.
- [convenience init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>, device: HKDevice?, metadata: [String : Any]?)](hkcorrelation/init(type:start:end:objects:device:metadata:).md)
  Instantiates and returns a new correlation instance with the provided device and metadata.
### Getting Correlation Data
- [var correlationType: HKCorrelationType](hkcorrelation/correlationtype.md)
  The type for this correlation.
- [var objects: Set<HKSample>](hkcorrelation/objects.md)
  The set of sample objects that make up the correlation.
- [func objects(for: HKObjectType) -> Set<HKSample>](hkcorrelation/objects(for:).md)
  Returns a set containing all the objects of the specified type in the correlation.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathCorrelation: String](hkpredicatekeypathcorrelation.md)
  The key path for accessing the object’s correlation inside a predicate format string.

## Relationships

### Inherits From
- [HKSample](hksample.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HKCumulativeQuantitySample](hkcumulativequantitysample.md)
  A sample that represents a cumulative quantity.
- [class HKDiscreteQuantitySample](hkdiscretequantitysample.md)
  A sample that represents a discrete quantity.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKCategorySample](hkcategorysample.md)
  A sample with values from a short list of possible values.
- [Units and quantities](units-and-quantities.md)
  Objects used to specify a quantity for a given unit, and to convert between units.
- [Metadata Keys](metadata-keys.md)
  Constants used to add metadata to objects stored in HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelation)*