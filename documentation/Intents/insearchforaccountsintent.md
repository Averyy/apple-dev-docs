# INSearchForAccountsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A user request for information about their accounts in your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INSearchForAccountsIntent
```

```objc
@interface INSearchForAccountsIntent : INIntent
```

#### Overview

Siri creates an instance of [`INSearchForAccountsIntent`](./insearchforaccountsintent.md) when the user asks for information about accounts available in your app. Users can ask for information about monetary and nonmonetary accounts. For example, an airline app might allow the user to search for an account that manages their frequent flier miles. The user can ask for information such as a list of accounts or the balance of a specific account. Use the data the intent provides to find the user’s accounts and return the information the user requests.

To process the request, your handler must adopt the [`INSearchForAccountsIntentHandling`](./insearchforaccountsintenthandling.md) protocol. When your implementation confirms the request, provide an instance of [`INSearchForAccountsIntentResponse`](./insearchforaccountsintentresponse.md) that includes the accounts that meet the user’s critieria. If the search is successful, Siri offers the user a way to view the results.

[`INSearchForAccountsIntent`](./insearchforaccountsintent.md) is only available to Siri Intents and requires an unlocked device before processing. Siri performs the following actions automatically:

- Requests the user’s confirmation before passing the request to your app or Intents extension for processing.
- Asks the user to unlock a locked device.

##### Example Phrases

Users can ask Siri to search for accounts in a variety of ways. Although not exhaustive, the following table provides a few sample phrases, in different languages, that you can use when testing your intents.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| `en` | How much money is in my checking account? | How many points are on my credit card? |
| `zh_CN` | 我的支票账户里面有多少钱 | 我的信用卡上面有多少点数 |
| `zh_HK` | 我嘅支票戶口入面有幾多錢 | 我嘅信用卡入面有幾多積分點數 |
| `zh_TW` | 存款帳戶裡有多少錢 | 我信用卡上有多少點數 |
| `yue_CN` | 我嘅支票户口入面有几多钱 | 我嘅信用卡入面有几多积分点数 |
| `ar` | كم من المال في حسابي بالبنك الوطني | كم نقطة على بطاقة الائتمان الخاصة بي |
| `da` | hvor mange penge er der i min lønkonto | hvor mange points er på mit kreditkort |
| `de` | Wie viel Geld ist auf meinem Girokonto | Wie viele Punkte habe ich mit meiner Kreditkarte gesammelt. |
| `es` | ¿Cuánto dinero tengo en mi cuenta corriente? | Dime cuántos puntos tiene mi tarjeta de crédito |
| `fi` | Kuinka paljon minulla on rahaa käyttötilillä | Kuinka monta bonuspistettä on luottokortillani |
| `fr` | Combien y a-t-il sur mon compte courant | Combien de points y a-t-il sur ma carte de crédit |
| `he` | כמה כסף יש בחשבון החסכון שלי | כמה נקודות יש בכרטיס אשראי שלי |
| `it` | Quanti soldi ci sono nel mio conto bancario | Quanti punti ho sulla mia carta di credito |
| `ja` | チェッキング口座にお金はいくらある | クレジットカードのポイントはどれくらい |
| `ko` | 통장에 돈 얼마나 있어 | 신용카드에 포인트 얼마나 있어 |
| `ms` | Berapa banyak wang dalam akaun semasa saya | Berapakah mata pada kad kredit saya |
| `nb` | Hvor mye penger er det på brukskontoen min | Hvor mange poeng har jeg på kredittkortet |
| `nl` | Hoeveel geld heb ik op mijn betaalrekening | Hoeveel punten staan er op mijn creditcard. |
| `pt` | Quanto dinheiro tem na minha conta corrente | Quantos pontos tem no meu cartão de crédito |
| `ru` | Сколько денег на моём текущем счету | Сколько бонусных баллов на моей кредитной карточке |
| `sv` | Hur mycket pengar finns det på mitt bankkonto | Hur många poäng har jag på mitt kreditkort |
| `th` | ฉันมีเงินอยู่ในบัญชีกระแสรายวันอยู่เท่าไหร่ | ฉันมีแต้มบัตรเครดิตเท่าไหร่ |
| `tr` | Birikim hesabımda ne kadar bakiye var | Kredi kartımda ne kadar puan var |

## Topics

### Initializing the Intent Object
- [init(accountNickname: INSpeakableString?, accountType: INAccountType, organizationName: INSpeakableString?, requestedBalanceType: INBalanceType)](./insearchforaccountsintent/init%28accountnickname,accounttype,organizationname,requestedbalancetype%29.md)
  Initializes the intent object with the specified search parameters.
### Getting the Search Attributes
- [var accountNickname: INSpeakableString?](./insearchforaccountsintent/accountnickname.md)
  The nickname that the user assigned to the account.
- [var accountType: INAccountType](./insearchforaccountsintent/accounttype.md)
  The type of the account.
- [var organizationName: INSpeakableString?](./insearchforaccountsintent/organizationname.md)
  The name of an organization attached to the account.
- [var requestedBalanceType: INBalanceType](./insearchforaccountsintent/requestedbalancetype.md)
  The balance type requested by the user.
- [enum INBalanceType](./inbalancetype.md)
  Constants indicating the meaning of a balance.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Search for Accounts
- [protocol INSearchForAccountsIntentHandling](./insearchforaccountsintenthandling.md)
  The handler interface for searching for account information.
- [class INSearchForAccountsIntentResponse](./insearchforaccountsintentresponse.md)
  Your app’s response to a request to search for account information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintent)*