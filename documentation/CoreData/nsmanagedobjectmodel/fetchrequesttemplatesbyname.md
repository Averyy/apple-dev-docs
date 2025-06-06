# fetchRequestTemplatesByName

**Framework**: Core Data  
**Kind**: property

A dictionary of the receiver’s fetch request templates, keyed by name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fetchRequestTemplatesByName: [String : NSFetchRequest<any NSFetchRequestResult>] { get }
```

#### Discussion

If the template contains a predicate with substitution variables, you should instead use [`fetchRequestFromTemplate(withName:substitutionVariables:)`](nsmanagedobjectmodel/fetchrequestfromtemplate(withname:substitutionvariables:).md) to create a new fetch request.

## See Also

- [func fetchRequestTemplate(forName: String) -> NSFetchRequest<any NSFetchRequestResult>?](nsmanagedobjectmodel/fetchrequesttemplate(forname:).md)
  Returns the fetch request with a specified name.
- [func fetchRequestFromTemplate(withName: String, substitutionVariables: [String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?](nsmanagedobjectmodel/fetchrequestfromtemplate(withname:substitutionvariables:).md)
  Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.
- [func setFetchRequestTemplate(NSFetchRequest<any NSFetchRequestResult>?, forName: String)](nsmanagedobjectmodel/setfetchrequesttemplate(_:forname:).md)
  Associates the specified fetch request with the receiver using the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplatesbyname)*