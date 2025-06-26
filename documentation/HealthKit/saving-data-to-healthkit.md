# Saving data to HealthKit

**Framework**: HealthKit

Create and share HealthKit samples.

#### Overview

Your app can create new samples and add them to the HealthKit store. Although all sample types follow a similar procedure, each type has its own variations:

1. Look up the type identifier for your data. For example, to record the user’s weight, you use the [`bodyMass`](hkquantitytypeidentifier/bodymass.md) type identifier. For the complete list of type identifiers, see [`Data types`](data-types.md).
2. Use the convenience methods on the [`HKObjectType`](hkobjecttype.md) class to create the correct object type for your data. For example, to save the user’s weight, you’d create an [`HKQuantityType`](hkquantitytype.md) object using the [`quantityType(forIdentifier:)`](hkobjecttype/quantitytype(foridentifier:).md) method. For a list of convenience methods, see [`HKObjectType`](hkobjecttype.md).
3. Instantiate an object of the matching [`HKSample`](hksample.md) subclass using the object type.
4. Save the object to the HealthKit store using the [`save(_:withCompletion:)`](hkhealthstore/save(_:withcompletion:)-6fmtg.md) method.

Each [`HKSample`](hksample.md) subclass has its own convenience methods for instantiating sample objects, which modify the steps described in the list above.

![An illustration showing how a quality sample relates to its identifier, type, and quantity.](https://docs-assets.developer.apple.com/published/4eca8a6c5bfd4d688c10ba510d59385c/media-2943340%402x.png)

For quantity samples, create an instance of the [`HKQuantity`](hkquantity.md) class. The quantity’s units must correspond to the allowable units described in the type identifier’s documentation. For example, the [`height`](hkquantitytypeidentifier/height.md) documentation states that it uses length units. Therefore, your quantity must use centimeters, meters, feet, inches, or another compatible unit. For more information, see [`HKQuantitySample`](hkquantitysample.md).

![An illustration showing how a category sample relates to its identifier, type, and value.](https://docs-assets.developer.apple.com/published/ff590914b31e464e30b64cf30413ee43/media-2943344%402x.png)

For category samples, the sample’s value must correspond to the enum described in the type identifier’s documentation. For example, the [`sleepAnalysis`](hkcategorytypeidentifier/sleepanalysis.md) documentation states that it uses the [`HKCategoryValueSleepAnalysis`](hkcategoryvaluesleepanalysis.md) enum. Therefore, you must pass a value from this enum when creating this sample. For more information, see [`HKCategorySample`](hkcategorysample.md).

![An illustration showing how a correlation sample relates to its identifier, type, and contained objects.](https://docs-assets.developer.apple.com/published/d4efeeeba2c6d6eb376574444efdab63/media-2943342%402x.png)

For correlations, you must first create all the sample objects that the correlation will contain. The correlation’s type identifier describes both the type and the number of objects that can be contained. Don’t save the contained objects into the HealthKit store. They’re stored as part of the correlation. For more information, see [`HKCorrelation`](hkcorrelation.md).

> ❗ **Important**:  In iOS 17.2 and later, the Journal app encourages people to reflect on their day-to-day experiences, including physical accomplishments, workouts, and emotions and moods. If your app saves data to HealthKit, high-level summaries of that data can appear as suggestions in the Journal app, or in other apps that use the [`Journaling Suggestions`](https://developer.apple.com/documentation/JournalingSuggestions) framework.

##### Balance Performance and Details

When saving data to the HealthKit store, you often need to choose between using a single sample to represent the data or splitting the data across multiple, smaller samples. A single, long sample is better from a performance perspective; however, multiple smaller samples gives the user a more detailed look into how their data changes over time. Ideally, you want to find a sample size that’s granular enough to provide the user with useful historical data and you should avoid saving samples that are 24 hours long or longer.

When recording a workout, you can use high frequency data (a minute or less per sample) to provide intensity charts and otherwise analyze the user’s performance over the workout. For less intensive activity, like daily step counts, samples of an hour or less often work best. This lets you produce meaningful daily and hourly graphs.

Most sample types have restrictions on duration. If you attempt to save a sample that doesn’t meet those restrictions, it fails to save. For more details on checking the duration restrictions, refer to [`HKSampleType`](hksampletype.md).

##### Work with Data in the Health App

The Health app gives users access to all of the data in their HealthKit store. Users can view, add, delete, and manage their data.

Specifically, users can:

- See a dashboard containing their current health data.
- Access all the data stored in HealthKit. Users can view the data by type, by app, or by device.
- Manage each app’s permission to read and write from the HealthKit store.

As a result, the Health app has a few important impacts on developing HealthKit apps. First, remember that users can always modify their data outside your app or even change your permission to access their data. As a result, your app should always query for the current data in the HealthKit store or perform background queries to track changes to the store.

Second, you can also use the Health app to view the data your app is saving to the HealthKit store. This can be particularly useful during early testing, to verify that your app is saving everything as expected.

## See Also

- [Reading data from HealthKit](reading-data-from-healthkit.md)
  Use queries to request sample data from HealthKit.
- [class HKHealthStore](hkhealthstore.md)
  The access point for all data managed by HealthKit.
- [Creating a Mobility Health App](creating-a-mobility-health-app.md)
  Create a health app that allows a clinical care team to send and receive mobility data.
- [Data types](data-types.md)
  Specify the kind of data used in HealthKit.
- [Samples](samples.md)
  Create and save health and fitness samples.
- [Queries](queries.md)
  Query health and fitness data.
- [Visualizing HealthKit State of Mind in visionOS](visualizing-healthkit-state-of-mind-in-visionos.md)
  Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.
- [Logging symptoms associated with a medication](logging-symptoms-associated-with-a-medication.md)
  Fetch medications and dose events from the HealthKit store, and create symptom samples to associate with them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/saving-data-to-healthkit)*