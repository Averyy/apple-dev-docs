# About the HealthKit framework

**Framework**: HealthKit

Learn about the architecture and design of the HealthKit framework.

#### Overview

Share health and fitness data between apps using the HealthKit framework. Rather than developers creating custom data types and units, HealthKit constrains data types and units to a predefined list. This ensures that all apps understand what the data means and how they can use it.

Additionally, the framework uses a large number of subclasses, producing deep hierarchies of similar classes. Often, these classes have subtle but important differences between them. For example, you use an [`HKQuantitySample`](hkquantitysample.md) object to store data with a numeric value and an [`HKCategorySample`](hkcategorysample.md) object to store a value selected from an enumeration.

HealthKit also uses pairs of closely related classes that you need to use together. For example, the [`HKObject`](hkobject.md) and [`HKObjectType`](hkobjecttype.md) abstract classes have largely parallel hierarchies of concrete subclasses. When working with objects and object types, you must use matching subclasses.

##### Healthkit Data

HealthKit saves a variety of data types in the HealthKit Store:

##### Properties of Objects and Samples

The [`HKObject`](hkobject.md) class is the superclass of all HealthKit sample types. All [`HKObject`](hkobject.md) subclasses are immutable. Each object has the following properties:

The [`HKSample`](hksample.md) class is a subclass of [`HKObject`](hkobject.md). Sample objects represent data at a particular point in time, and all sample objects are subclasses of the [`HKSample`](hksample.md) class. They have the following properties:

Samples are further divided into four concrete subclasses:

##### Threading

The HealthKit store is thread-safe, and most HealthKit objects are immutable. In general, you can use HealthKit safely in a multithreaded environment.

> **Note**:  All the HealthKit API’s completion handlers execute on private background queues. You typically dispatch this data back to the main queue before updating your user interface or changing any other resources that you can only safely modify from the main thread.

For more information about multithreading and concurrent programming, see [`Concurrency Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

##### Syncing Data Between Devices

iPhone, Apple Watch, and visionOS each have their own HealthKit store. iPadOS 17 and later also has its own HealthKit store. It is also available on iPadOS apps running on Vision Pro. HealthKit automatically syncs data between these devices. To save space, old data is periodically purged from Apple Watch. Use [`earliestPermittedSampleDate()`](hkhealthstore/earliestpermittedsampledate().md) to determine the earliest samples available on Apple Watch.

While the HealthKit framework is available on iPadOS 16 and earlier and on MacOS 13 and later, these devices don’t have a copy of the HealthKit store. This means you can include HealthKit code in apps running on these devices, simplifying the creation of multiplatform apps. However, they can’t read or write HealthKit data, and calls to [`isHealthDataAvailable()`](hkhealthstore/ishealthdataavailable().md) return [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [Setting up HealthKit](setting-up-healthkit.md)
  Set up and configure your HealthKit store.
- [Authorizing access to health data](authorizing-access-to-health-data.md)
  Request permission to read and share data in your app.
- [Protecting user privacy](protecting-user-privacy.md)
  Respect and safeguard your user’s privacy.
- [HealthKit updates](../Updates/HealthKit.md)
  Learn about important changes to HealthKit.
- [HealthKitUI](../healthkitui/healthkitui.md)
  Display user interface that enables a person to view and interact with their health data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/about-the-healthkit-framework)*