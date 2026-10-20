# fetchRequestTemplate(forName:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the fetch request with a specified name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fetchRequestTemplate(forName name: String) -> NSFetchRequest<any NSFetchRequestResult>?
```

```objc
- (NSFetchRequest *) fetchRequestTemplateForName:(NSString *) name;
```

#### Return Value

The fetch request named `name`.

#### Discussion

If the template contains substitution variables, you should instead use [`fetchRequestFromTemplate(withName:substitutionVariables:)`](./fetchrequestfromtemplate%28withname,substitutionvariables%29.md) to create a new fetch request.

## Parameters

- `name`: A string containing the name of a fetch request template.

## See Also

### Manipulating fetch request templates
- [var fetchRequestTemplatesByName: [String : NSFetchRequest<any NSFetchRequestResult>]](./fetchrequesttemplatesbyname.md)
  A dictionary of the receiver’s fetch request templates, keyed by name.
- [func fetchRequestFromTemplate(withName: String, substitutionVariables: [String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?](./fetchrequestfromtemplate%28withname,substitutionvariables%29.md)
  Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.
- [func setFetchRequestTemplate(NSFetchRequest<any NSFetchRequestResult>?, forName: String)](./setfetchrequesttemplate%28_,forname%29.md)
  Associates the specified fetch request with the receiver using the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplate(forname:))*