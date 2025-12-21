# FinanceKit

**Framework**: FinanceKit  
**Kind**: module

Access financial data and interact with Apple Card, Apple Cash, and orders in Wallet.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

#### Overview

Use FinanceKit to access on-device financial data, Apple Cash, and interact with orders in Apple Wallet.

You interact with FinanceKit through [`FinanceStore`](financestore.md) and [`FinanceKitUI`](https://developer.apple.com/documentation/FinanceKitUI), which presents a standardized UI that people access.

![Image of FinanceKit hero logo.](https://docs-assets.developer.apple.com/published/7c9c9fc964649ae4b55466327fde7c07/financekit-hero-img.png)

Using the FinanceKit framework, you can:

- Access on-device financial data.
- Add, update, store, and interact with orders in Wallet.
- Interact with Apple Card and Apple Cash.

> ❗ **Important**: To access someone’s financial data, you must meet the criteria outlined in [`Get started with FinanceKit`](https://developer.apple.comhttps://developer.apple.com/financekit/), request the [`FinanceKit managed entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/financekit/), hold an organization-level Apple Developer account, be logged in as Account Holder, and include the `NSFinancialDataUsageDescription` string in your `Info.plist`. Apple reviews each application using [`Get started with FinanceKit`](https://developer.apple.comhttps://developer.apple.com/financekit/). If your request meets the criteria, Apple adds the entitlement to your developer account by using managed capabilities. To request access, see the [`FinanceKit managed entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/financekit/). For more information about managed entitlements, see [`Provisioning with capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities).

## Topics

### Essentials
- [Implementing a background delivery extension](implementing-a-background-delivery-extension.md)
  Receive up-to-date financial data in your app and its extensions by adding a background delivery extension.
- [FinanceKit updates](../Updates/FinanceKit.md)
  Learn more about changes to FinanceKit.
### Data storage
- [class FinanceStore](financestore.md)
  Secure storage for Apple Wallet orders.
### Authorization
- [func authorizationStatus() async throws -> AuthorizationStatus](financestore/authorizationstatus.md)
  Checks the authorization status for the calling application.
- [func requestAuthorization() async throws -> AuthorizationStatus](financestore/requestauthorization.md)
  Prompts a person to give FinanceKit authorization to access financial data.
- [enum AuthorizationStatus](authorizationstatus.md)
### Accounts
- [func accounts(query: AccountQuery) async throws -> [Account]](financestore/accounts(query:).md)
  Returns a list of accounts a person added to their Wallet that meet the criteria in the provided account query.
- [func accountHistory(since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Account>](financestore/accounthistory(since:ismonitoring:).md)
  Returns a list of accounts a person added since a time specified by the provided financial history token.
- [struct AssetAccount](assetaccount.md)
  A structure that describes the characteristics of an asset account.
- [struct LiabilityAccount](liabilityaccount.md)
  A structure that describes the characteristics of a liability account.
- [enum Account](account.md)
  A structure that describes a financial account.
### Balances
- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](financestore/accountbalances(query:).md)
  Returns a list of balances that meet the criteria in the provided account query.
- [func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>](financestore/accountbalancehistory(foraccountid:since:ismonitoring:).md)
  Returns the account balance history since a time specified by the provided financial history token.
- [struct AccountBalance](accountbalance.md)
  A structure that describes the financial balance of an account at a specific point in time. The financial balance of an account at a specific point in time.
- [struct AccountBalanceQuery](accountbalancequery.md)
  A structure that defines an account balance query.
- [struct Balance](balance.md)
  A structure that describes an account balance.
- [enum CreditDebitIndicator](creditdebitindicator.md)
  Values that the framework uses to describe transactions as credits or debits.
- [enum CurrentBalance](currentbalance.md)
  Values that describe the state of an account’s credit balance.
### Orders
- [struct FullyQualifiedOrderIdentifier](fullyqualifiedorderidentifier.md)
  A structure that specifies the characteristics of an order.
- [func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult](financestore/saveorder(signedarchive:).md)
  Adds an order to the store or updates an existing order.
### Transactions
- [func transactionHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Transaction>](financestore/transactionhistory(foraccountid:since:ismonitoring:).md)
  Returns the transactions for the specified account ID, optional starting time, and monitoring indicator for long running transaction queries.
- [func transactions(query: TransactionQuery) async throws -> [Transaction]](financestore/transactions(query:).md)
  Returns transactions that match the provided transaction query.
- [struct AccountQuery](accountquery.md)
  A structure that defines an account query.
- [struct AccountCreditInformation](accountcreditinformation.md)
  A structure that describes the credit information associated with an account.
- [struct CurrencyAmount](currencyamount.md)
  A structure that describes a monetary amount and its currency.
- [struct Transaction](transaction.md)
  A structure that represents a transaction relating to a specific financial account.
- [struct TransactionQuery](transactionquery.md)
  A structure that describes the parameters to use for a transaction query.
- [enum TransactionType](transactiontype.md)
  Values that describe kinds of transactions.
- [enum TransactionStatus](transactionstatus.md)
  Values that describe the status of a transaction.
### Queries
- [FinanceStore.HistoryToken](financestore/historytoken.md)
  A structure that describes the starting point to use for financial data queries.
### Merchant categories
- [struct MerchantCategoryCode](merchantcategorycode.md)
### Errors
- [enum FinanceError](financeerror.md)
  Values that describe errors that may occur when accessing financial data.
### Protocols
- [protocol BackgroundDeliveryExtension](backgrounddeliveryextension.md)
  An extension used to receive updates about changes to data within the finance store.
- [protocol BackgroundDeliveryExtensionProviding](backgrounddeliveryextensionproviding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/FinanceKit)*