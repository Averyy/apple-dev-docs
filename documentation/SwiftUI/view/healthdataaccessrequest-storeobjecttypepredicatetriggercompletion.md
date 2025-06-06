# healthDataAccessRequest(store:objectType:predicate:trigger:completion:)

**Framework**: SwiftUI  
**Kind**: method

Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@preconcurrency
nonisolated func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType, predicate: NSPredicate? = nil, trigger: some Equatable, completion: @escaping (Result<Bool, any Error>) -> Void) -> some View
```

#### Discussion

Some samples require per-object authorization. For these samples, people can select which ones your app can read on a sample-by-sample basis. By default, your app can read any of the per-object authorization samples that it has saved to the HealthKit store; however, you may not always have access to those samples. People can update the authorization status for any of these samples at any time.

Your app can begin by setting up the request in SwiftUI.

```swift
@State private var trigger = false
let store = HKHealthStore()

var body: some Scene {
    WindowGroup {
        ContentView(enabled: $authenticated)
            .healthDataAccessRequest(store: store,
                                     objectType: .visionPrescriptionType(),
                                     predicate: nil,
                                     trigger: trigger) { result in

                switch result {
                case .success(_):
                    authenticated = true
                case .failure(let error):
                    // Handle the error here.
                    fatalError("*** An error occurred while requesting authentication: \(error) ***")
                }

                logger.debug("Authentication Complete.")
            }
    }
}
```

Next, query for any samples that it already has permission to read.

```swift
// Read the newest prescription from the HealthKit store.
let queryDescriptor = HKSampleQueryDescriptor(predicates: [.visionPrescription()],
                                              sortDescriptors: [SortDescriptor(\.startDate, order: .reverse)],
                                              limit: 1)

let prescription: HKVisionPrescription

do {
    guard let result = try await queryDescriptor.result(for: store).first else {
        print("*** No prescription found. ***")
        return
    }

    prescription = result
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while reading the most recent vision prescriptions: \(error.localizedDescription) ***")
}
```

Based on the results, you can then decide whether you need to request authorization for additional samples. Modify the trigger’s value to prompt someone to modify the samples your app has access to read.

```swift
// Request authorization for additional samples.
trigger.toggle()
```

> ❗ **Important**: Using the [`healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)`](View/healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:).md) method to request read access to any data types that require per-object authorization fails with an [`errorInvalidArgument`](https://developer.apple.com/documentation/healthkit/hkerror/2320686-errorinvalidargument) error.

Using the [`healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)`](View/healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:).md) method to request read access to any data types that require per-object authorization fails with an [`errorInvalidArgument`](https://developer.apple.com/documentation/healthkit/hkerror/2320686-errorinvalidargument) error.

When your app calls this method, HealthKit displays an authorization sheet that asks for permission to read the samples that match the predicate and object type. The person using your app can then select individual samples to share with your app. The system always asks for permission, regardless of whether the user previously granted it.

People can individually enable each of the prescriptions. After they respond, the system calls the callback handler on an arbitrary background queue.

## Parameters

- `store`: The HealthKit store where you’re requesting authorization.
- `objectType`: The data type you want to read. This type must be a type that requires per-object authorization.
- `predicate`: An optional predicate that further restricts the objects of interest.
- `trigger`: A value used to trigger the request. This value must be a    variable.   Any change to the variable triggers a request.
- `completion`: A block that the system calls after the request is complete. The system passes the result parameter.

## See Also

- [func healthDataAccessRequest(store: HKHealthStore, readTypes: Set<HKObjectType>, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:readtypes:trigger:completion:).md)
  Requests permission to read the specified HealthKit data types.
- [func healthDataAccessRequest(store: HKHealthStore, shareTypes: Set<HKSampleType>, readTypes: Set<HKObjectType>?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:sharetypes:readtypes:trigger:completion:).md)
  Requests permission to save and read the specified HealthKit data types.
- [func workoutPreview(WorkoutPlan, isPresented: Binding<Bool>) -> some View](view/workoutpreview(_:ispresented:).md)
  Presents a preview of the workout contents as a modal sheet


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/healthdataaccessrequest(store:objecttype:predicate:trigger:completion:))*