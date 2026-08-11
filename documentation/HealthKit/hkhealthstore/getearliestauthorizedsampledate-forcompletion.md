# getEarliestAuthorizedSampleDate(for:completion:)

**Framework**: HealthKit  
**Kind**: method

Returns the earliest date that the person permits your app to read samples for the given data types.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func getEarliestAuthorizedSampleDate(for types: Set<HKObjectType>, completion: @escaping @Sendable ([HKObjectType : Date]?, (any Error)?) -> Void)
```

## Mentions

- [Authorizing access to health data](authorizing-access-to-health-data.md)

#### Discussion

This method derives the earliest sample date from availability in the HealthKit store as well as from the time frame a person chooses in the authorization prompt.

Call this method after requesting authorization to determine whether the person restricts your app’s read access to a time window as opposed to the full available history. Adjust your app’s workflow to work with less data. In particular, if the person limits your app’s access, ensure that any trends, baselines, or anomaly detections your app offers work from partial data.

When someone grants limited access to a data type, this method returns the earliest date from which your app can read samples of that type. HealthKit evaluates the boundary against a sample’s end date, so the framework might service your query with a sample that begins before the earliest authorization date as long as the sample ends after it. Treat all data before that date as unknown — not an absence of data — because a full history may exist outside the range your app is permitted to read.

If your app has full access to a type, or if the person denies access, this method returns no entry for that type in the resulting dictionary. Your app can’t distinguish between denied and full access; limited authorization is the only state your app can identify, by design. The dictionary that this method produces is empty if no type has limited access. HealthKit omits a type from the result when:

- Your app doesn’t have read access for the type.
- Your app has full read access to the type.
- Your app has limited read access but no specific earliest readable date is available.

To distinguish between a type that you request but has no time boundary and a type that isn’t part of your request at all, compare the returned dictionary’s keys against your input set. A type that appears in your input set but not in the result either has full access or no access; the framework doesn’t silently skip a type.

If your app makes inferences on partial data, consider informing people that granting full access improves your app’s experience.

> **Note**: This method reflects data access that’s scoped by the person’s choices in the authorization prompt. By contrast, [`earliestPermittedSampleDate()`](hkhealthstore/earliestpermittedsampledate().md) returns the earliest date HealthKit permits any app to save or query samples, regardless of what someone authorizes.

#### Adjust Queries for Limited Authorization

If your app queries HealthKit data by date range, consider incorporating the returned dates into your query predicate. If your app uses [`HKAnchoredObjectQuery`](hkanchoredobjectquery.md) with a saved anchor, the anchor automatically  scopes the query to changes since the last fetch.

For each type your app queries, compare your intended query start date and the authorization date for that type and use whichever is later. This ensures that the query requests just the data your app needs. Varying types can have a different earliest date, so calculate the date per type, as shown here:

```swift
let types: Set<HKObjectType> = [HKQuantityType(.stepCount)]
let authorizationDates = try await store.earliestAuthorizedSampleDate(for: types)

let intendedStartDate = Date().addingTimeInterval(-90 * 24 * 3600)
let authorizationDate = authorizationDates[HKQuantityType(.stepCount)]
let queryStartDate = [intendedStartDate, authorizationDate]
    .compactMap { $0 }
    .max() ?? intendedStartDate

let predicate = HKQuery.predicateForSamples(
    withStart: queryStartDate,
    end: .now,
    options: .strictStartDate
)
```

## Parameters

- `types`: The set of [`HKObjectType`](hkobjecttype.md) values to query. HealthKit omits any type that doesn’t have a limited-access earliest date from the result.
- `completion`: A closure with a dictionary parameter that maps qualifying types to their earliest readable date, or an error on failure.

## See Also

- [func authorizationStatus(for: HKObjectType) -> HKAuthorizationStatus](hkhealthstore/authorizationstatus(for:).md)
  Returns the app’s authorization status for sharing the specified data type.
- [enum HKAuthorizationStatus](hkauthorizationstatus.md)
  Constants indicating the authorization status for a particular data type.
- [func getRequestStatusForAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>, completion: (HKAuthorizationRequestStatus, (any Error)?) -> Void)](hkhealthstore/getrequeststatusforauthorization(toshare:read:completion:).md)
  Indicates whether the system presents the user with a permission sheet if your app requests authorization for the provided types.
- [enum HKAuthorizationRequestStatus](hkauthorizationrequeststatus.md)
  Values that indicate whether your app needs to request authorization from the user.
- [class func isHealthDataAvailable() -> Bool](hkhealthstore/ishealthdataavailable.md)
  Returns a Boolean value that indicates whether HealthKit is available on this device.
- [func supportsHealthRecords() -> Bool](hkhealthstore/supportshealthrecords.md)
  Returns a Boolean value that indicates whether the current device supports clinical records.
- [func requestAuthorization(toShare: Set<HKSampleType>?, read: Set<HKObjectType>?, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/requestauthorization(toshare:read:completion:).md)
  Requests permission to save and read the specified data types.
- [func requestAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>) async throws](hkhealthstore/requestauthorization(toshare:read:).md)
  Asynchronously requests permission to save and read the specified data types.
- [func requestPerObjectReadAuthorization(for: HKObjectType, predicate: NSPredicate?, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/requestperobjectreadauthorization(for:predicate:completion:).md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func handleAuthorizationForExtension(completion: (Bool, (any Error)?) -> Void)](hkhealthstore/handleauthorizationforextension(completion:).md)
  Requests permission to save and read the data types specified by an extension.
- [var authorizationViewControllerPresenter: UIViewController?](hkhealthstore/authorizationviewcontrollerpresenter.md)
  The view controller that presents HealthKit authorization sheets.
- [func earliestAuthorizedSampleDate(for: Set<HKObjectType>) async throws -> [HKObjectType : Date]](hkhealthstore/earliestauthorizedsampledate(for:).md)
  Returns the earliest date that the person permits your app to read samples for the given data types.
- [func earliestPermittedSampleDate() -> Date](hkhealthstore/earliestpermittedsampledate.md)
  Returns the earliest date that the framework permits your app to save or read samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/getearliestauthorizedsampledate(for:completion:))*