# WebContentSettings.FilterPolicy.specific(_:)

**Framework**: Managed Settings  
**Kind**: case  
**Role**: Case

The policy blocks the specified domains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case specific(Set<WebDomain>)
```

## Discussion

Your app can block up to 50 web domains at once.

## See Also

### Providing filters and exceptions
- [WebContentSettings.FilterPolicy.all(except:)](./all%28except%29.md)
  The system blocks all websites except the ones you specify.
- [case auto(Set<WebDomain>, except: Set<WebDomain>)](./auto%28_,except%29.md)
  The system blocks adult content.
- [WebContentSettings.FilterPolicy.none](./none.md)
  The policy doesn’t affect any domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy/specific(_:))*