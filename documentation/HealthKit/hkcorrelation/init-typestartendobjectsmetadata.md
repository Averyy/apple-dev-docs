# init(type:start:end:objects:metadata:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a new correlation instance with the provided metadata.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(type correlationType: HKCorrelationType, start startDate: Date, end endDate: Date, objects: Set<HKSample>, metadata: [String : Any]?)
```

#### Discussion

Use a correlation object to represent composite data—that is, a sample that requires more than a single value. To create a correlation sample, first create the quantity and category samples you intend to combine into the correlation. Next, create the correlation’s type. Finally, instantiate the correlation, passing in the type, start date, end date, samples, and metadata as shown below.

Use this method when you need to include additional metadata, but the data was not recorded using external hardware. Samples representing food should always include metadata with the [`HKMetadataKeyFoodType`](hkmetadatakeyfoodtype.md) key.

**Swift**:

```swift
let date = NSDate();
 
// Create a sample for calories
 
guard let calorieType = HKObjectType.quantityTypeForIdentifier(HKQuantityTypeIdentifierDietaryEnergyConsumed) else {
    fatalError("*** Unable to create the calorie type ***")
}
 
let calorieQuantity =
    HKQuantity(unit: HKUnit.kilocalorieUnit(), doubleValue: 110.0)
 
let calorieSample = HKQuantitySample(type: calorieType,
                                     quantity: calorieQuantity, startDate: date, endDate: date)
 
// Create a sample for total fat
 
guard let fatType = HKObjectType.quantityTypeForIdentifier(HKQuantityTypeIdentifierDietaryFatTotal) else {
    fatalError("*** Unable to create the fat type ***")
}
 
let fatQuantity =
    HKQuantity(unit: HKUnit.gramUnit(), doubleValue: 0.0)
 
let fatSample = HKQuantitySample(type: fatType,
                                 quantity: fatQuantity, startDate: date, endDate: date)
 
// Create a sample for carbohydrates
 
guard let carbohydratesType = HKObjectType.quantityTypeForIdentifier(HKQuantityTypeIdentifierDietaryCarbohydrates) else {
    fatalError("*** Unable to create the carbohydrates type ***")
}
 
let carbohydratesQuantity =
    HKQuantity(unit: HKUnit.gramUnit(), doubleValue: 30.0)
 
let carbohydratesSample = HKQuantitySample(type: carbohydratesType,
                                           quantity: carbohydratesQuantity, startDate: date, endDate: date)
 
// Create a sample for protein
 
guard let proteinType = HKObjectType.quantityTypeForIdentifier(HKQuantityTypeIdentifierDietaryProtein) else {
    fatalError("*** Unable to create the protein type ***")
}
 
let proteinQuantity =
    HKQuantity(unit: HKUnit.gramUnit(), doubleValue: 1.0)
 
let proteinSample = HKQuantitySample(type: proteinType,
                                     quantity: proteinQuantity, startDate: date, endDate: date)
 
// Create the food sample
 
let objects: Set = [calorieSample, fatSample, carbohydratesSample, proteinSample]
 
let metadata = [HKMetadataKeyFoodType: "Banana"]
 
guard let bananaType = HKObjectType.correlationTypeForIdentifier(HKCorrelationTypeIdentifierFood) else {
    fatalError("*** Unable to create the banana type ***")
}
 
let banana = HKCorrelation(type: bananaType,
                           startDate: date, endDate: date, objects: objects, metadata:metadata)
```

**Objective-C**:

```objc
NSDate *date = [NSDate date];
 
// Create sample for calories
 
HKQuantityType *calorieType = [HKObjectType quantityTypeForIdentifier:
    HKQuantityTypeIdentifierDietaryEnergyConsumed];
 
HKQuantity *calorieQuantity =
[HKQuantity quantityWithUnit:[HKUnit kilocalorieUnit] doubleValue:110.0];
 
HKQuantitySample *calorieSample =
[HKQuantitySample quantitySampleWithType:calorieType
                                quantity:calorieQuantity
                               startDate:date
                                 endDate:date];
 
// Create sample for total fat
 
HKQuantityType *fatType = [HKObjectType quantityTypeForIdentifier:
    HKQuantityTypeIdentifierDietaryFatTotal];
 
HKQuantity *fatQuantity =
[HKQuantity quantityWithUnit:[HKUnit gramUnit] doubleValue:0.0];
 
HKQuantitySample *fatSample =
[HKQuantitySample quantitySampleWithType:fatType
                                quantity:fatQuantity
                               startDate:date
                                 endDate:date];
 
// Create sample for carbohydrates
 
HKQuantityType *carbohydratesType = [HKObjectType quantityTypeForIdentifier:
    HKQuantityTypeIdentifierDietaryCarbohydrates];
 
HKQuantity *carbohydratesQuantity =
[HKQuantity quantityWithUnit:[HKUnit gramUnit] doubleValue:30.0];
 
HKQuantitySample *carbohydratesSample =
[HKQuantitySample quantitySampleWithType:carbohydratesType
                                quantity:carbohydratesQuantity
                               startDate:date
                                 endDate:date];
 
// Create sample for protein
 
HKQuantityType *proteinType = [HKObjectType quantityTypeForIdentifier:
    HKQuantityTypeIdentifierDietaryProtein];
 
HKQuantity *proteinQuantity =
[HKQuantity quantityWithUnit:[HKUnit gramUnit] doubleValue:30.0];
 
HKQuantitySample *proteinSample =
[HKQuantitySample quantitySampleWithType:proteinType
                                quantity:proteinQuantity
                               startDate:date
                                 endDate:date];
 
// Create food sample
 
NSSet *objects = [NSSet setWithObjects:calorieSample, fatSample,
                  carbohydratesSample, proteinSample, nil];
 
NSDictionary *metadata = @{HKMetadataKeyFoodType: @"Banana"};
 
HKCorrelationType *bananaType = [HKObjectType correlationTypeForIdentifier:
    HKCorrelationTypeIdentifierFood];
 
HKSample *banana = [HKCorrelation correlationWithType:bananaType
                                            startDate:date
                                              endDate:date
                                              objects:objects metadata:metadata];
```

## Parameters

- `correlationType`: The type for this correlation. For a complete list of correlation types, see Correlation Types.
- `startDate`: The start date for the sample. This date must be equal to or earlier than the end date; otherwise, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)).
- `endDate`: The end date for the sample. This date must be equal to or later than the start date; otherwise, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)).
- `objects`: A set of [`HKSample`](hksample.md) objects. Specifically, this set contains the quantity and category samples to be grouped into this correlation.
- `metadata`: The metadata dictionary containing extra information that describes this correlation. The dictionary’s keys are all [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects . The values may be [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), or [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) objects. For a complete list of predefined metadata keys, see [`Metadata Keys`](metadata-keys.md). Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create custom keys as needed to extend the HealthKit sample’s capabilities. When creating correlations representing food, always use the [`HKMetadataKeyFoodType`](hkmetadatakeyfoodtype.md) key to provide the food’s name.

## See Also

- [var objects: Set<HKSample>](hkcorrelation/objects.md)
  The set of sample objects that make up the correlation.
- [class func correlationType(forIdentifier: HKCorrelationTypeIdentifier) -> HKCorrelationType?](hkobjecttype/correlationtype(foridentifier:).md)
  Returns the shared correlation type for the provided identifier.
- [var endDate: Date](hksample/enddate.md)
  The sample’s end date.
- [var correlationType: HKCorrelationType](hkcorrelation/correlationtype.md)
  The type for this correlation.
- [var metadata: [String : Any]?](hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [convenience init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>)](hkcorrelation/init(type:start:end:objects:).md)
  Instantiates and returns a new correlation instance.
- [convenience init(type: HKCorrelationType, start: Date, end: Date, objects: Set<HKSample>, device: HKDevice?, metadata: [String : Any]?)](hkcorrelation/init(type:start:end:objects:device:metadata:).md)
  Instantiates and returns a new correlation instance with the provided device and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelation/init(type:start:end:objects:metadata:))*