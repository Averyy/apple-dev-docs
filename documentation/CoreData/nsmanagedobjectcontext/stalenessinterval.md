# stalenessInterval

**Framework**: Core Data  
**Kind**: property

The maximum length of time that may have elapsed since the store previously fetched data before fulfilling a fault issues a new fetch.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var stalenessInterval: TimeInterval { get set }
```

#### Discussion

The staleness interval controls whether  uses data previously fetched by the application, or issues a new fetch (see also [`refresh(_:mergeChanges:)`](nsmanagedobjectcontext/refresh(_:mergechanges:).md)). The staleness interval does  affect objects currently in use (that is, it is  used to automatically update property values from a persistent store after a certain period of time).

The expiration value is applied on a per object basis. It is the relative time until cached data (snapshots) should be considered stale. For example, a value of 300.0 informs the context to utilize cached information for no more than 5 minutes after an object was originally fetched.

Note that the staleness interval is a hint and may not be supported by all persistent store types. It is not used by XML and binary stores, because these stores maintain all current values in memory.

The default is a negative value, which represents infinite staleness allowed. `0.0` represents “no staleness acceptable”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/stalenessinterval)*