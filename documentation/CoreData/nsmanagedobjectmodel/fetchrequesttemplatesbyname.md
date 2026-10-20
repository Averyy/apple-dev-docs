# fetchRequestTemplatesByName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A dictionary of the receiver’s fetch request templates, keyed by name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fetchRequestTemplatesByName: [String : NSFetchRequest<any NSFetchRequestResult>] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,NSFetchRequest *> * fetchRequestTemplatesByName;
```

#### Discussion

If the template contains a predicate with substitution variables, you should instead use [`fetchRequestFromTemplate(withName:substitutionVariables:)`](./fetchrequestfromtemplate%28withname,substitutionvariables%29.md) to create a new fetch request.

## See Also

### Manipulating fetch request templates
- [func fetchRequestTemplate(forName: String) -> NSFetchRequest<any NSFetchRequestResult>?](./fetchrequesttemplate%28forname%29.md)
  Returns the fetch request with a specified name.
- [func fetchRequestFromTemplate(withName: String, substitutionVariables: [String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?](./fetchrequestfromtemplate%28withname,substitutionvariables%29.md)
  Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.
- [func setFetchRequestTemplate(NSFetchRequest<any NSFetchRequestResult>?, forName: String)](./setfetchrequesttemplate%28_,forname%29.md)
  Associates the specified fetch request with the receiver using the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplatesbyname)*